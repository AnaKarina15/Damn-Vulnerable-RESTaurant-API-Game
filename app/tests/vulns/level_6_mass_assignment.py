import json

from db.models import User, UserRole


def test_mass_assignment_privilege_escalation(test_db, customer_client):
    """
    Note:
        The `/profile` PATCH endpoint is vulnerable to mass-assignment.
        By sending extra properties in the JSON body like
        `"additionalProp1": {"role": "Chef"}` the server applies
        the modified payload and the user's role is escalated to Chef.

    Possible fix:
        Do not allow unknown fields to be applied directly to the ORM model.
        Explicitly whitelist updatable fields in `patch_profile` or use
        a Pydantic model that rejects unexpected fields.

        The fix could be implemented in `app/apis/auth/services/patch_profile_service.py`
        by validating allowed attributes before calling `setattr` on the user.
    """

    # the `customer_client` fixture already creates a user with username "customer"
    # PATCH /profile updates the currently authenticated user, so target that user
    current = test_db.query(User).filter_by(username="customer").first()
    assert current is not None

    # craft payload that sets `role` directly to exploit mass-assignment
    payload = {"role": "Chef"}

    response = customer_client.patch(f"/profile", content=json.dumps(payload))
    assert response.status_code == 200

    # reload user from DB to observe changes made by the endpoint
    updated = test_db.query(User).filter_by(username="customer").first()
    assert updated.role == "Chef"
