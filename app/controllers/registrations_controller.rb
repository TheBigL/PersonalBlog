class RegistrationsController < Devise::RegistrationsController
    private

    def sign_up_params

      @User =  params.require(:user).permit(:username, :email, :password, :password_confirmation)
      if @user.save
        UserMailer.registration_confirmation(@user).deliver

    end



    def account_update_params
        params.require(:user).permit(:username, :email, :password, :password_confirmation, :currentpassword)
    end

end
