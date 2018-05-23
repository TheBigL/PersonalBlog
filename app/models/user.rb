class User < ApplicationRecord
  include RoleModel
  
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable and :omniauthable
  devise :database_authenticatable, :registerable, :recoverable, :rememberable, :trackable, :validatable
  has_many :posts
  has_one_attached :avatar

  after_initialize :set_default_role, :if => :new_record?
  def set_default_role
    self.role ||= :user
  end

  def admin?
    self.role == "admin"
  end

  def contributor?
    self.role == "contributor"
  end

  def user?
    self.role == "user"
  end

end
