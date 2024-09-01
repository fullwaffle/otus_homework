from flask import Blueprint, jsonify, request, redirect, url_for
from models.models import Owner, Pet, db

api = Blueprint("api", __name__)


@api.route("/api/owners", methods=["GET"])
def get_owners():
    owners = Owner.query.all()
    return jsonify(
        [
            {
                "id": owner.id,
                "name": owner.name,
                "age": owner.age,
                "phone": owner.phone,
                "pets": [
                    {"id": pet.id, "name": pet.name, "breed": pet.breed, "age": pet.age}
                    for pet in owner.pets
                ],
            }
            for owner in owners
        ]
    )

@api.route("/api/owner", methods=["POST"])
def create_owner():
    owner_name = request.form.get("owner-name")
    owner_age = int(request.form.get("owner-age"))
    owner_phone = int(request.form.get("owner-phone"))

    owner = Owner(name=owner_name, age=owner_age, phone=owner_phone)
    db.session.add(owner)
    db.session.commit()

    new_url = url_for("views.index")
    return redirect(new_url, code=201)


@api.route("/api/pets", methods=["GET"])
def get_pets():
    pets = Pet.query.all()
    return jsonify(
        [
            {
                "id": pet.id,
                "name": pet.name,
                "breed": pet.breed,
                "age": pet.age,
                "owner": (
                    {"id": pet.owner.id, "name": pet.owner.name} if pet.owner else None
                ),
            }
            for pet in pets
        ]
    )


@api.route("/api/owners_without_pets", methods=["GET"])
def get_owners_without_pets():
    owners = Owner.query.outerjoin(Pet).filter(Pet.id == None).all()
    return jsonify(
        [
            {"id": owner.id, "name": owner.name, "age": owner.age, "phone": owner.phone}
            for owner in owners
        ]
    )


@api.route("/api/pets_without_owners", methods=["GET"])
def get_pets_without_owners():
    pets = Pet.query.filter(Pet.owner_id == None).all()
    return jsonify(
        [
            {"id": pet.id, "name": pet.name, "breed": pet.breed, "age": pet.age}
            for pet in pets
        ]
    )
