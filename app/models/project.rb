class Project < ApplicationRecord
  extend FriendlyId
  friendly_id :title, use: :slugged
  has_many :images

  def weburl?
    !weburl.empty?
  end

  def giturl?
    !giturl.empty?
  end
end
