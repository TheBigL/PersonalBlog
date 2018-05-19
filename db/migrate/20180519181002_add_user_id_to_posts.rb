class AddUserIdToPosts < ActiveRecord::Migration[5.2]
  def change
    add_column :posts, :userID, :integer
  end
end
