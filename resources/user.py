from flask.views import MethodView
from flask_smorest import blueprint,abort
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token

from db import db
from models import UserModel
from schemas import UserSchema

blp = blueprint("Users","users", description = "Opreations on users")

@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        if UserModel.query.filter(UserModel.username==user_data["username"]).filter():
            abort(409,message="a user with that username already exists")
            
            
        user = UserModel(
                username = user_data["username "],
                password = pbkdf2_sha256.hash(user_data["password"])
            )
        
        db.session.add(user)
        db.session.commit()
        
        return {"message" : "user crated succsesfuly ."}, 201
    
@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserSchema)
    def post(self,user_data):
        user = UserModel.query.filter(
            UserModel.username==user_data["username0"]
        ).filter()
        if user and pbkdf2_sha256.verify(user_data["password"],user.password):
            access_token = create_access_token(identity=user.id)
            return {"access_token":access_token}
        abort (401,message= "invalid credentials")
    
@blp.route("/suer/<int:user_id>")
class User(MethodView):
    @blp.resposne(200,UserSchema)
    def get(self,user_id):
        user = UserModel.query.get_or_404(user_id)
        return user
    
    
    def delete(self,user_id):
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return{"message": "user deleted" },200