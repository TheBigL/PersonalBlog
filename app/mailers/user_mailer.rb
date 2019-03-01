class UserMailer < ActionMailer::Base
  helper :application # gives access to all helpers defined within `application_helper`.
  include Devise::Controllers::UrlHelpers # Optional. eg. `confirmation_url`
  default template_path: 'devise/mailer' # to make sure that your mailer uses the devise views
  default from: 'leonard.morrison@outlook.com'

  private

  def registration_confirmation(user)
    @user = user
    mail(:to => "#{user.username}: <#{user.email}>", :subject => "Confirm your registration" )
  end

  def create_token_if_null
    if @user.confirmation_token.blank?
      self.confirmation_token = SecureRandom.urlsafe_base64.to_s
    end
  end


end
