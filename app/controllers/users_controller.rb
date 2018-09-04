class UsersController < ApplicationController
before_filter :authenticate_user!
after_action :verify_authorized

    def destroy
        user = User.find(params[:id])

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
