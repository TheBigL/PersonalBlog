class RemoveConfirmables < ActiveRecord::Migration[5.2]
  def change
    remove_column :users, :confirmation_token, :string
    remove_column :users, :email_confirmed, :boolean, :default => false
    remove_column :users, :confirmed_at, :datetime
    remove_column :users, :unconfirmed_email, :string
    # remove_column :users, :reset_password_token, :string
    remove_column :users, :reset_password_sent_at, :datetime
    remove_column :users, :remember_created_at, :datetime
    remove_column :users, :reset_password_token, :string
    remove_column :users, :confirmation_sent_at, :datetime
    remove_column :users, :sign_in_count, :integer
    # remove_column :users, :reset_password_sent_at, :datetime
    # remove_column :users, :confirmation_sent_at, :datetime

    # remove_index :users, name: "index_users_on_reset_password_token"
  end
end
