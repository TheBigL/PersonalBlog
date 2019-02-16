class UserMailer < ApplicationMailer



  def account_activation(user)
    @user = user
    mail to: user.email, subject: "User Activation", from: 'leonard.morrison@outlook.com'
  end


end
