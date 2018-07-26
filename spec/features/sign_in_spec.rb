require 'rails_helper'

feature 'Sign In', :devise do
    scenario 'user cannnot sign in if the email is invalid' do
        sign_in('person@example.com', 'password')
        expect(page).to have_content 'Invalid email or password'


end