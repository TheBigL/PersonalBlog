class PostPolicy < ApplicationPolicy
  
  

  

  class PolicyScope < Scope
    include Pundit
    rescue_from Pundit::NotAuthorizedError, with: :user_not_authorized
    

    attr_reader :user, :record

    def initialize_user(current_user, record)
      @user = current_user
      @post = record
    end

    def resolve
      if @user.role == "admin"
        scope.all
      end
    end
    
  end

  def show?
    true
  end

  def index?
    true
  end

  def create?
    record.user.role == "admin"? && record.user == @user?
  end

  def update?
    @user.present? && @user.role == "admin"? || @user.role == "contributor"?
  end

  def destroy?
    @user.present? && @user.admin? || @post.user_id == @user.user_id?
  end

  private

  def user_not_authorized
    flash[:alert] = "Can't let you do that, " + @user.username + "!"
  end

end
