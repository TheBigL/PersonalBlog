class RemoveUserIdIndex < ActiveRecord::Migration[5.2]
  def change
    remove_index :comments, :user_id
    
  end
end
