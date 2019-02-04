class UserMailer < 'Devise::Mailer'

  helper :application # gives access to all helpers defined within `application_helper`.
  include Devise::Controllers::UrlHelpers # Optional. eg. `confirmation_url`
  default template_path: 'devise/mailer' # to make sure that your mailer uses the devise views
  
  default :from => "leonard.morrison@outlook.com"

  def registration_confirmation(user)
      @user = user
      mail(:to => "#{user.username} <#{user.email}>", :subject => "Thanks for registering to my blog!")
  end
end
