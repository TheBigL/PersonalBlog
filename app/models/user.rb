class User < ApplicationRecord
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable and :omniauthable
  devise :database_authenticatable, :registerable, :recoverable,
  :rememberable, :trackable, :validatable

  belongs_to :role
  after_save :setup_role
  has_many :posts
  has_many :comments



  def setup_role
    if self.username == "LeonardMorrison"
      self.role_id = 1
    else
      self.role_id = 3
    end
  end
















end
