class RemoveConfirmables < ActiveRecord::Migration[5.2]
  def change
    remove_column :users, :confirmation_token, :string
    remove_column :users, :email_confirmed, :boolean, :default => false
    remove_column :users, :confirmed_at, :datetime
    remove_column :users, :unconfirmed_email, :string
  end
end
