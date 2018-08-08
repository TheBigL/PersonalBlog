class ApplicationController < ActionController::Base
    include Pundit
    rescue_from Pundit::NotAuthorizedError, with: :user_not_authorized
    protect_from_forgery with: :exception
    before_action :configure_permitted_parameters, if: :devise_controller?


    def about

    end
  
    protected
  
    def configure_permitted_parameters
      added_attrs = [ :username, :email, :password, :password_confirmation　]
      devise_parameter_sanitizer.permit :sign_up, keys: added_attrs
      devise_parameter_sanitizer.permit :account_update, keys: added_attrs
      devise_parameter_sanitizer.permit :sign_in, keys: added_attrs
    end

    private
    def user_not_authorized
      flash[:alert] = "You aren't authorized to go to that page. Contact Leban Mohamed through email at leban.mohamed@live.ca."
      redirect_to (request.referrer || root_path)
    end
        
end
