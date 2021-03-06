class CommentsController < ApplicationController
    before_action :set_post
    def create
        set_post
        # Create associated model, just like we did in the console before
        @comment = @post.comments.build(comment_params.merge({:post_id => @post.post_id, :user_id => current_user.user_id}))
        # We want to show the comment in the context of the Post
        # @comment.post_id = @post.post_id
        # @comment.user_id = current_user.user_id
        @comment.save
        redirect_to @post
    end


    def update
        @comment = set_comment
        @comment.update(comment_params)
        redirect_to @post
    end

    def destroy
        @comment = set_comment
        @comment.destroy
        redirect_to @post
    end

    private
    def comment_params
        params.require(:comment).permit(:content)
    end

    def set_post
        @post = Post.friendly.find(params[:post_id])
    end

    def set_comment
        @comment = Comment.find(params[:id])
    end
end
