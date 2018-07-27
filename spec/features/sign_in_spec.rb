require 'rails_helper'

feature 'Sign In', :devise do
    scenario "user cannnot sign in if the user isn't registered" do
        signin('person@example.com', 'password')
        expect(page).to have_content 'Invalid email or Password.'
    end

    scenario "User can log in with valid credentials" do
        user = FactoryBot.create(:user)
        signin(user.email, user.password)
        expect(page).to have_content 'Signed in successfully'
    end

    scenario "User cannot sign in with an invalid email" do
        user = FactoryBot.create(:user)
        signin('invalid@email.com', user.password)
        expect(page).to have_content 'Invalid Email or Password.'
    end

    scenario "User cannot sign in with an invalid email" do
        user = FactoryBot.create(:user)
        signin(user.email, 'invalid')
        expect(page).to have_content 'Invalid Email or Password.'
    end



end