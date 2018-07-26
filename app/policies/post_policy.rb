class PostPolicy < ApplicationPolicy
  

  

  class PolicyScope < Scope

    attr_reader :user, :record

    def initialize_user(user, record)
      @user = user
      @post = record
    end

    def resolve
      if user.role == "admin"
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
    @user.present? && @user.admin? || @user.role == "contributor"
  end

end
