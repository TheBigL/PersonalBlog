class UsersController < ApplicationController
    def destroy
        @user = User.find(params[:id])
        @user.destroy
    
        if @user.destroy
            redirect_to root_url, notice: "The user has been deleted..."
        end

    end


end
