class CommentsController < ApplicationController
    def create
        @post = Post.find(params[:post_id])
        # Create associated model, just like we did in the console before
        @comment = @post.comments.create(comment_params)
        # We want to show the comment in the context of the Post
        redirect_to @post
    end
    private
    def comment_params
        params.require(:comment).permit(:name, :content)
    end
end
