# -*- coding: utf-8 -*-
"""Emergent LLM integration for AgentScope Friday agent."""
import os
from typing import Union, Sequence, Optional, List, Any, Dict
import asyncio
from dotenv import load_dotenv

from agentscope.model import ChatModelBase
from agentscope.message import Msg
from agentscope.formatter import FormatterBase, OpenAIChatFormatter

# Load environment variables
load_dotenv()

try:
    from emergentintegrations.llm.chat import LlmChat, UserMessage
except ImportError as e:
    raise ImportError(
        "emergentintegrations package is required. "
        "Install it with: pip install emergentintegrations --extra-index-url https://d33sy5i8bnduwe.cloudfront.net/simple/"
    ) from e


class EmergentChatModel(ChatModelBase):
    """A chat model wrapper for Emergent LLM integration."""
    
    def __init__(
        self,
        api_key: str,
        provider: str = "openai",
        model_name: str = "gpt-4o",
        session_id: str = "friday-session",
        system_message: str = "You are a helpful assistant.",
        **kwargs
    ):
        """Initialize the Emergent Chat Model.
        
        Args:
            api_key: The Emergent universal API key
            provider: LLM provider (openai, anthropic, gemini)
            model_name: Model name to use
            session_id: Session identifier
            system_message: System message for the agent
            **kwargs: Additional arguments
        """
        self.api_key = api_key
        self.provider = provider.lower()
        self.model_name = model_name
        self.session_id = session_id
        self.system_message = system_message
        
        # Initialize the LlmChat client
        self.chat = LlmChat(
            api_key=self.api_key,
            session_id=self.session_id,
            system_message=self.system_message
        ).with_model(self.provider, self.model_name)
        
        super().__init__(
            model_name=model_name,
            **kwargs
        )
    
    def __call__(
        self,
        messages: Sequence[Msg],
        **kwargs
    ) -> Msg:
        """Synchronous call to the model."""
        return asyncio.run(self.async_call(messages, **kwargs))
    
    async def async_call(
        self,
        messages: Sequence[Msg],
        **kwargs
    ) -> Msg:
        """Asynchronous call to the model."""
        try:
            # Convert AgentScope messages to text
            user_content = ""
            for message in messages:
                if hasattr(message, 'content'):
                    if isinstance(message.content, str):
                        user_content += message.content + "\n"
                    elif isinstance(message.content, dict) and 'text' in message.content:
                        user_content += message.content['text'] + "\n"
                    else:
                        user_content += str(message.content) + "\n"
                else:
                    user_content += str(message) + "\n"
            
            # Create user message
            user_message = UserMessage(text=user_content.strip())
            
            # Send message and get response
            response = await self.chat.send_message(user_message)
            
            # Create response message
            return Msg(
                name="assistant",
                content=response,
                role="assistant"
            )
            
        except Exception as e:
            error_msg = f"Error calling Emergent LLM: {str(e)}"
            return Msg(
                name="assistant", 
                content=error_msg,
                role="assistant"
            )
    
    def format(
        self,
        *args,
        **kwargs
    ) -> Union[List[dict], str]:
        """Format messages for the model."""
        # Use OpenAI format as default
        formatter = OpenAIChatFormatter()
        return formatter.format(*args, **kwargs)


def get_emergent_model(provider: str, model_name: str, api_key: str) -> EmergentChatModel:
    """Get an Emergent model instance."""
    return EmergentChatModel(
        api_key=api_key,
        provider=provider,
        model_name=model_name,
        session_id="friday-agent-session",
        system_message="You are Friday, a helpful assistant specialized in daily task management and AgentScope framework support."
    )


def get_emergent_formatter(provider: str) -> FormatterBase:
    """Get formatter for Emergent models."""
    # Use OpenAI formatter as default since emergentintegrations handles the conversion
    return OpenAIChatFormatter()