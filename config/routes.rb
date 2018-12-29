Rails.application.routes.draw do
  mount Ckeditor::Engine => '/ckeditor'
  devise_for :users, controllers: { registrations: "registrations"}
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  resources :posts

  get    '/comments',          to: 'comments#index', as: 'comments'
  post   '/comments',          to: 'comments#create'
  get    '/comments/new',      to: 'comments#new',   as: 'new_comment'
  get    '/comments/:id',      to: 'comments#show',  as: 'comment'
  get    '/comments/:id/edit', to: 'comments#edit',  as: 'edit_comment'
  patch  '/comments/:id',      to: 'comments#update'
  delete '/comments/:id',      to: 'comments#destroy'

  root "posts#index"

  get '/users', to: 'users#index', as: 'users'
  get '/users/:id', to: 'users#show', as: 'user'
  patch '/users/:id', to: 'users#update', as: 'edit_user'
  delete '/users/:id', to: 'users#destroy'


end
