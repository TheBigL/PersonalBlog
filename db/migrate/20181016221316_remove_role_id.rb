class RemoveRoleId < ActiveRecord::Migration[5.2]
  def change
    remove_index nil, name: "index_users_on_roleId" 
  end
end
