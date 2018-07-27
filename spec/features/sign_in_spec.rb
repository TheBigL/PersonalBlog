require 'rails_helper'

feature 'Sign In', :devise do
    scenario "user cannnot sign in if the user isn't registered" do
        sign_in('person@example.com', 'password')
        expect(page).to have_content 'Invalid email or password'
    end

    scenario "User can log in with valid credentials" do
        user = FactoryBot.create(:user)
        sign_in(user.email, user.password)
        expect(page).to have_content 'Signed in successfully'
    end



end