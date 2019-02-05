class RegistrationsController < Devise::RegistrationsController
    private

    def sign_up_params
      if @user.
        UserMailer.confirmation_instructions(@user).deliver
      end

    end
    def account_update_params
        params.require(:user).permit(:username, :email, :password, :password_confirmation, :currentpassword)
    end

end
