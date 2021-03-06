class PostsController < ApplicationController
    before_action :authenticate_user!, except: [:index, :show]

    after_action :verify_authorized, except: [:index, :show]

    def index
     @posts = Post.order(created_at: :desc).page(params[:page]).per(10)
    end

    def by_creation
      @posts = Post.order(created_at: :asc).page(params[:page]).per(10)
    end

    def new
     @post = current_user.posts.build
     @post.user_id = current_user.user_id
     authorize @post
    end

    def show
     set_post
    end

    def edit
     set_post
     authorize @post
    end

    def update
     set_post
     authorize @post
     @post.update(post_params)
     redirect_to @post
    end

    def destroy
     set_post
     authorize @post
     @post.destroy

     redirect_to action: "index"
    end

    def upvote
        @post.upvote_from current_user
        authorize @post
    end

    def downvote
        @post.downvote_from current_user
        authorize @post
    end



    def create
        @post = current_user.posts.build(post_params)
        authorize @post
        respond_to do |format|
            if @post.save
                format.html {redirect_to @post, notice: 'Blog post has been posted!'}
                format.json {render :show, status: :created, location: @post}
            else
                format.html {render :new}
                format.json {render json: @post.errors, status: :unprocessable_entity}
            end
        end

    end

    private
      def post_params
          params.require(:post).permit(:title, :content, :header_image, :upload)
      end

      def set_post
          @post = Post.find_by_slug(params[:id])
      end

end
