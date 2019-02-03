Rails.application.routes.draw do
  get 'projects/index'
  get 'projects/show'
  get 'projects/new'
  get 'projects/update'
  get 'projects/destroy'
  mount Ckeditor::Engine => '/ckeditor'
  devise_for :users, controllers: { registrations: "registrations"}
  resources :users
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  resources :posts do
    resources :comments
  end
  resources :projects



  root "posts#index"


end
