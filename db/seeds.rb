# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)
admin = Role.create( role_id: 1, roleName: "Admin")

admin.save!

contributor = Role.create(role_id: 2, roleName: "Contributor")


contributor.save!


registeredUser = Role.create(role_id: 3, roleName: "RegisteredUser")

registeredUser.save!

user = User.new
user.username = "LeonardMorrison"
user.email = "leonard.morrison@outlook.com"
user.role_id = 1
user.password = "StarFox1993"
user.password_confirmation = "StarFox1993"
user.save
