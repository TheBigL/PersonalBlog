class UserMailer < Devise::Mailer

  helper :application # gives access to all helpers defined within `application_helper`.
  include Devise::Controllers::UrlHelpers # Optional. eg. `confirmation_url`
  default template_path: 'devise/mailer' # to make sure that your mailer uses the devise views

  default :from => "leonard.morrison@outlook.com"

  def confirmation_instructions(user)
    @user = user
    mail(:to => 'leonard.morrison@outlook.com', :subject => "Welcome to my blog! Click here to register.")
  end
end
