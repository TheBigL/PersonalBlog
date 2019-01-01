class PostsController < ApplicationController
    before_action :authenticate_user!, except: [:index, :show]

    after_action :verify_authorized, except: [:index, :show]

    def index
     @posts = Post.order(created_at: :desc).page(params[:page]).per(10)
     #authorize @posts
    end

    def new
     @post = current_user.posts.build
     authorize @post
     if @post.save
      redirect_to @post, notice: 'Post was successfully created.'
    else
      render :new
    end
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

     redirect_to action: "index", notice: "The post was removed"
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
          params.require(:post).permit(:title, :content, :header_image, uploads: [])
      end

      def set_post
          @post = Post.friendly.find(params[:id])
    #    authorize @post
      end

end
