class Project < ApplicationRecord
  extend FriendlyId
  friendly_id :title, use: :slugged
  has_many :images


  def picture_url
    if !more.empty?
      self
    elsif weburl?
      weburl
    else
      giturl
    end
  end

  def weburl?
    !weburl.empty?
  end

  def giturl?
    !giturl.empty?
  end
end
