class PostPolicy < ApplicationPolicy
  
  def show?
    true
  end

  def index?
    true
  end

  def create?
    return true if user.present? && user.admin? || user.contributor?
  end

  def update?
    return true if user.present? && user.admin? || user.contributor?
  end

  def destroy?
    return true if user.present? && user.admin? || user.contributor?
  end

end
