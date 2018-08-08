class AddPostIdToComments < ActiveRecord::Migration[5.2]
  def change
    add_column :comments, :post_id, :integer
    add_column :posts, :post_id, :integer
    add_index :comments, :post_id
    add_index :posts, :post_id
  end
end
