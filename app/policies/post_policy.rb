class PostPolicy < ApplicationPolicy
  
  def show?
    true
  end

  def index?
    true
  end

  def create?
    user.present? && user.admin? || user.contributor?
  end

  def update?
    user.present? && user.admin? || user.contributor?
  end

  def destroy?
    user.present? && user.admin? || user.contributor?
  end

end
