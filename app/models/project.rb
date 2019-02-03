class Project < ApplicationRecord
  extend FriendlyId
  friendly_id :title, use: :slugged
  has_one_attached :image

  def weburl?
    !weburl.empty?
  end

  def giturl?
    !giturl.empty?
  end
end
