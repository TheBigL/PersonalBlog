class UsersController < ApplicationController
    def destroy
        set_user
        @user.destroy
    
        if @user.destroy
            redirect_to root_url, notice: "The user has been deleted..."
        end

    end

    def update
        @user = User.find(params[:id])
    end


    private 
    def set_user
        @user = User.find(params[:id])
    end



end
