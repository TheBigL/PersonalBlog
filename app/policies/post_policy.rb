class PostPolicy < ApplicationPolicy
  

  attr_reader :current_user, :model

  def initialize_user(current_user, model)
   @current_user = current_user
   @user = model
  end

  def show?
    true
  end

  def index?
    true
  end

  def create?
    return true if @current_user.present? && @current_user.role == "admin"? || @current_user.role == "contributor"?
  end

  def update?
    return true if @current_user.present? && @current_user.role == "admin"? || @current_user.role == "contributor"?
  end

  def destroy?
    return true if user.present? && user.admin? || user.contributor?
  end

  def cf_content
    [ :Admin, :Contributor, :User, :Banned ]
   end

end
