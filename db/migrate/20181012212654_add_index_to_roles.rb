class AddIndexToRoles < ActiveRecord::Migration[5.2]
  def change
    add_index :roles, roleId
    add_index :users, roleId
    remove_column :roles, roleId
  end
end
