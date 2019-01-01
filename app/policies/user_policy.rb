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
      is_admin?
    end

    def index?
     is_admin?
    end

    def update?
      is_admin?
      :notice => "The User has been updated."
    end

    def destroy?
      is_admin?
      redirect_to users_path, :notice => "User has been deleted"
    end

    private
    def user_not_authorized
      flash[:alert] = "You cannot access this part of this site. Only Admins can access this site!"
    end

    def is_admin?
      @current_user.role_id == 1
    end



  end
end
end
