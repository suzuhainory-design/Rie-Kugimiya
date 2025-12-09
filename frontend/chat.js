// Chat application logic
class ChatApp {
    constructor() {
        this.config = null;
        this.conversationHistory = [];
        this.isProcessing = false;
        
        this.initElements();
        this.attachEventListeners();
        this.loadSavedConfig();
    }
    
    initElements() {
        // Config elements
        this.configPanel = document.getElementById('configPanel');
        this.providerSelect = document.getElementById('provider');
        this.apiKeyInput = document.getElementById('apiKey');
        this.baseUrlInput = document.getElementById('baseUrl');
        this.baseUrlGroup = document.getElementById('baseUrlGroup');
        this.modelInput = document.getElementById('model');
        this.systemPromptTextarea = document.getElementById('systemPrompt');
        this.characterNameInput = document.getElementById('characterName');
        this.saveConfigBtn = document.getElementById('saveConfig');
        
        // Chat elements
        this.chatContainer = document.getElementById('chatContainer');
        this.chatTitle = document.getElementById('chatTitle');
        this.messagesDiv = document.getElementById('messages');
        this.userInput = document.getElementById('userInput');
        this.sendBtn = document.getElementById('sendBtn');
        this.showConfigBtn = document.getElementById('showConfig');
        this.messageRefs = new Map();
    }
    
    attachEventListeners() {
        this.providerSelect.addEventListener('change', () => {
            const isCustom = this.providerSelect.value === 'custom';
            this.baseUrlGroup.style.display = isCustom ? 'block' : 'none';
            
            // Update default models
            const defaults = {
                'openai': 'gpt-3.5-turbo',
                'anthropic': 'claude-3-5-sonnet-20241022',
                'deepseek': 'deepseek-chat',
                'custom': 'gpt-3.5-turbo'
            };
            this.modelInput.value = defaults[this.providerSelect.value];
        });
        
        this.saveConfigBtn.addEventListener('click', () => this.saveConfig());
        this.showConfigBtn.addEventListener('click', () => this.toggleView());
        this.sendBtn.addEventListener('click', () => this.sendMessage());
        this.userInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !this.isProcessing) {
                this.sendMessage();
            }
        });
    }
    
    loadSavedConfig() {
        const saved = localStorage.getItem('chatConfig');
        if (saved) {
            try {
                const config = JSON.parse(saved);
                this.providerSelect.value = config.provider || 'openai';
                this.apiKeyInput.value = config.api_key || '';
                this.baseUrlInput.value = config.base_url || '';
                this.modelInput.value = config.model || 'gpt-3.5-turbo';
                this.systemPromptTextarea.value = config.system_prompt || '';
                this.characterNameInput.value = config.character_name || 'Rie';
                
                // Trigger change event
                this.providerSelect.dispatchEvent(new Event('change'));
            } catch (e) {
                console.error('Failed to load config:', e);
            }
        }
    }
    
    saveConfig() {
        const apiKey = this.apiKeyInput.value.trim();
        if (!apiKey) {
            alert('Please enter API key');
            return;
        }
        
        this.config = {
            provider: this.providerSelect.value,
            api_key: apiKey,
            base_url: this.baseUrlInput.value.trim() || null,
            model: this.modelInput.value.trim(),
            system_prompt: this.systemPromptTextarea.value.trim(),
            character_name: this.characterNameInput.value.trim() || 'Rie'
        };
        
        localStorage.setItem('chatConfig', JSON.stringify(this.config));
        this.toggleView();
        this.enableChat();
    }
    
    toggleView() {
        const showChat = this.configPanel.style.display !== 'none';
        this.configPanel.style.display = showChat ? 'none' : 'block';
        this.chatContainer.style.display = showChat ? 'flex' : 'none';
        
        if (showChat && this.config) {
            this.chatTitle.textContent = `💬 Chat with ${this.config.character_name}`;
        }
    }
    
    enableChat() {
        this.userInput.disabled = false;
        this.sendBtn.disabled = false;
        this.userInput.focus();
    }
    
    addMessage(role, content, options = {}) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${role}`;
        messageDiv.textContent = content;

        if (options.recalled) {
            messageDiv.classList.add('recalled');
        }

        if (options.emotion) {
            messageDiv.classList.add(`emotion-${options.emotion}`);
        }

        if (options.messageId) {
            messageDiv.dataset.messageId = options.messageId;
        }

        this.messagesDiv.appendChild(messageDiv);
        this.scrollToBottom();
        
        return messageDiv;
    }
    
    scrollToBottom() {
        this.messagesDiv.scrollTop = this.messagesDiv.scrollHeight;
    }
    
    async sendMessage() {
        const text = this.userInput.value.trim();
        if (!text || this.isProcessing) return;
        
        this.isProcessing = true;
        this.userInput.value = '';
        this.userInput.disabled = true;
        this.sendBtn.disabled = true;
        
        // Add user message
        this.addMessage('user', text);
        this.conversationHistory.push({ role: 'user', content: text });
        
        try {
            // Call API
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    llm_config: this.config,
                    messages: this.conversationHistory,
                    character_name: this.config.character_name
                })
            });
            
            if (!response.ok) {
                throw new Error(`API error: ${response.status}`);
            }
            
            const data = await response.json();
            // Play message actions
            await this.playMessageActions(data.actions);
            
            // Update conversation history
            this.conversationHistory.push({
                role: 'assistant',
                content: data.raw_response
            });
            
        } catch (error) {
            // Try to get more detailed error info
            let errorMsg = error.message;
            if (error.message.includes('API error: 500')) {
                errorMsg = 'Server error. Please check:\n' +
                          '1. API key is valid\n' +
                          '2. Model name is correct\n' +
                          '3. Network connection\n' +
                          'Check browser console for details.';
            } else if (error.message.includes('API error: 401')) {
                errorMsg = 'Authentication failed. Please check your API key.';
            } else if (error.message.includes('API error: 404')) {
                errorMsg = 'Model not found. Please check the model name.';
            }

            this.addMessage('system', `Error: ${errorMsg}`);
            console.error('Chat error:', error);
        } finally {
            this.isProcessing = false;
            this.userInput.disabled = false;
            this.sendBtn.disabled = false;
            this.userInput.focus();
        }
    }
    
    async playMessageActions(actions) {
        for (const action of actions) {
            if (action.duration > 0) {
                await this.sleep(action.duration * 1000);
            }

            switch (action.type) {
                case 'pause':
                    // duration already awaited
                    break;

                case 'send': {
                    const messageDiv = this.addMessage('assistant', action.text, {
                        emotion: action.metadata?.emotion,
                        messageId: action.message_id
                    });

                    if (action.message_id) {
                        this.messageRefs.set(action.message_id, messageDiv);
                    }
                    break;
                }

                case 'recall': {
                    if (action.target_id && this.messageRefs.has(action.target_id)) {
                        const messageDiv = this.messageRefs.get(action.target_id);
                        if (messageDiv) {
                            messageDiv.classList.add('recalled');
                            setTimeout(() => {
                                messageDiv.remove();
                            }, 200);
                        }
                        this.messageRefs.delete(action.target_id);
                    }
                    break;
                }
            }
        }
    }
    
    sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
}

// Initialize app when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    new ChatApp();
});
