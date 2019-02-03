class ProjectPolicy < ApplicationPolicy
  class Scope < Scope
    def resolve
      scope
    end
  end

  def index?
    true
  end

  def show?
    true
  end

  def create?
    isLeonard?
  end

  def update?
    isLeonard?
  end

  def destroy?
    isLeonard?
  end



  private
  def isLeonard?
    @user.username == "LeonardMorrison"


end
