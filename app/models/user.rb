class User < ApplicationRecord
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable and :omniauthable
  devise :database_authenticatable, :registerable, :recoverable, :rememberable, :trackable, :validatable
  has_many :posts
  has_many :comments
  belongs_to :roles
  has_one_attached :avatar
  before_validation :set_default_role





  def set_default_role
     self.role_id = 3;
  end




end
