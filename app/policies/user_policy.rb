class UserPolicy < ApplicationPolicy

  class Scope < Scope
    include Pundit
    rescue_from Pundit::NotAuthorizedError, with: :user_not_authorized

    attr_reader :current_user, :model

    def initialize(current_user, model)
     @current_user = current_user
     @user = model
    end

    def show?
      current_user.role_id == 1? || @current_user == @user?
    end

    def index?
     current_user.role_id == 1?
    end

    def update?
      current_user.role_id == 1?
    end

    def destroy?
      user = User.find(params[:id])
      return false if @current_user.role_id != 1 and if @user == @current_user and if @user.role == "admin"
      user.destroy
      redirect_to users_path, :notice => "User has been deleted"
    end

    private
    def user_not_authorized
      flash[:alert] = "You cannot access this part of this site. Only Admins can access this site!"
    end



  end
end
end
