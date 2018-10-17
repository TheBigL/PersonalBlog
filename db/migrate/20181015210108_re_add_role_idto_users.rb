class ReAddRoleIdtoUsers < ActiveRecord::Migration[5.2]
  def change
    add_column :roles, :role_id, :integer
    add_column :users, :role_id, :integer
  end
end
