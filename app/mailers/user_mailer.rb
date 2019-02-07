class UserMailer < Devise::Mailer

  helper :application # gives access to all helpers defined within `application_helper`.
  include Devise::Controllers::UrlHelpers # Optional. eg. `confirmation_url`
  default template_path: 'devise/mailer' # to make sure that your mailer uses the devise views

  default :from => "leonard.morrison@outlook.com"

  def confirmation_instructions(@user, @user.confirmation_token, opts={})
  headers["Custom-header"] = "Bar"
  opts[:from] = 'leonard.morrison@outlook.com'
  opts[:reply_to] = 'leonard.morrison@outlook.com'
  super
  end
end
