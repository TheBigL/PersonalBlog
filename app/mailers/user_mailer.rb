class UserMailer < ActionMailer::Base

 default :from => "me@mydomain.com"

 def registration_confirmation(user)
    @user = user
    mail(:to => "#{user.username} <#{user.email}>", :subject => "Thanks for registering to my blog!")
 end
