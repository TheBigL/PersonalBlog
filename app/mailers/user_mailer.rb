class UserMailer < Devise::Mailer

  helper :application # gives access to all helpers defined within `application_helper`.
  include Devise::Controllers::UrlHelpers # Optional. eg. `confirmation_url`
  default template_path: 'devise/mailer' # to make sure that your mailer uses the devise views



  def account_activation(user)
    @user = user
    mail to: user.email, subject: "User Activation", from: 'leonard.morrison@outlook.com'

  end
end
