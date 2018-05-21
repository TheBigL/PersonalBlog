require 'test_helper'

class UsersControllerTest < ActionDispatch::IntegrationTest
  # test "the truth" do
  #   assert true
  # end

  #Test Sign up Controller
  it "Create a User" do
    user = User.create( email: 'testmcTesterson@test.com', username: 'Test', password: 'password123', password_confirmation: 'password')

  end
end
