Rails.application.routes.draw do
  mount Ckeditor::Engine => '/ckeditor'
  devise_for :users, controllers: { registrations: "users/registrations"}
  resources :users do
    get :confirm_token
  end
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  resources :posts do
    resources :comments
  end
  resources :projects



  root "posts#index"


end
