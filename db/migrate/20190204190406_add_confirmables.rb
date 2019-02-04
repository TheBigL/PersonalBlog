class AddConfirmables < ActiveRecord::Migration[5.2]
  def change
    add_column :users, :confirmation_token, :string
    add_column :users, :email_confirmed, :boolean, :default => false
    add_index :users, :confirmation_token,   unique: true
  end
end
